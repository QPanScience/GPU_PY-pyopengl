# Sample script to install Python and pip under Windows
# Authors: Olivier Grisel and Kyle Kastner
# License: CC0 1.0 Universal: http://creativecommons.org/publicdomain/zero/1.0/

$BASE_URL = "https://www.python.org/ftp/python/"
$GET_PIP_URL = "https://bootstrap.pypa.io/get-pip.py"
$GET_PIP_PATH = "C:\get-pip.py"


function DownloadPython ($python_version, $platform_suffix) {
    $webclient = New-Object System.Net.WebClient
    $filename = "python-" + $python_version + $platform_suffix + ".msi"
    $url = $BASE_URL + $python_version + "/" + $filename

    $basedir = $pwd.Path + "\"
    $filepath = $basedir + $filename
    if (Test-Path $filename) {
        Write-Host "Reusing" $filepath
        return $filepath
    }

    # Download and retry up to 5 times in case of network transient errors.
    Write-Host "Downloading" $filename "from" $url
    $retry_attempts = 3
    for($i=0; $i -lt $retry_attempts; $i++){
        try {
            $webclient.DownloadFile($url, $filepath)
            break
        }
        Catch [Exception]{
            Start-Sleep 1
        }
   }
   Write-Host "File saved at" $filepath
   return $filepath
}


function InstallPython ($python_version, $architecture, $python_home) {
    Write-Host "Installing Python" $python_version "for" $architecture "bit architecture to" $python_home
    if (Test-Path $python_home) {
        Write-Host $python_home "already exists, skipping."
        return $false
    }
    if ($architecture -eq "32") {
        $platform_suffix = ""
    } else {
        $platform_suffix = ".amd64"
    }
    $filepath = DownloadPython $python_version $platform_suffix
    Write-Host "Installing" $filepath "to" $python_home
    $args = "/qn /i $filepath TARGETDIR=$python_home"
    Write-Host "msiexec.exe" $args
    Start-Process -FilePath "msiexec.exe" -ArgumentList $args -Wait -Passthru
    Write-Host "Python $python_version ($architecture) installation complete"
    return $true
}


function InstallPip ($python_home) {
    $pip_path = $python_home + "/Scripts/pip.exe"
    $python_path = $python_home + "/python.exe"
    if (-not(Test-Path $pip_path)) {
        Write-Host "Installing pip..."
        $webclient = New-Object System.Net.WebClient
        $webclient.DownloadFile($GET_PIP_URL, $GET_PIP_PATH)
        Write-Host "Executing:" $python_path $GET_PIP_PATH
        Start-Process -FilePath "$python_path" -ArgumentList "$GET_PIP_PATH" -Wait -Passthru
    } else {
        Write-Host "pip already installed."
    }
}

function InstallCachedPackage($python_home, $pkg, $architecture){
    $pip_path = $python_home + "/Scripts/pip.exe"
    if ($architecture -eq "32") {
        $platform_suffix = "win32"
    } else {
        $platform_suffix = "amd64"
    }
    $python = $python_home+"\\python.exe"
    $python_version = ($python -c "import sys;print('py%s%s'%sys.version_info[:2])") | Out-String
    if (-not(Test-Path "c:\\tmp\\wheelhouse\\$pkg-$python_version-*$architecture*.whl")) {
        cmd /E:ON /V:ON /C .\\appveyor\\run_with_compiler.cmd $pip_path wheel -w c:\\tmp\\wheelhouse $pkg
    }
    $pip_path install -f c:\\tmp\\wheelhouse $pkg
    
}

function InstallPackage ($python_home, $pkg) {
    $pip_path = $python_home + "/Scripts/pip.exe"
    & $pip_path install $pkg
}

function main () {
    InstallPython $env:PYTHON_VERSION $env:PYTHON_ARCH $env:PYTHON
    InstallPip $env:PYTHON
    InstallPackage $env:PYTHON wheel
    InstallCachedPackage $env:PYTHON numpy $env:PYTHON_ARCH
}

main
