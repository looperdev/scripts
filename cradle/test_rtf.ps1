$cradleBin = "C:\Program Files\Cradle\bin\exe\windows\c_table.exe"
$args = "-login USERNAME,PASSWORD,DATABASE", "-file","c:\temp\temp.rtf", "-query", "temp_WRE_qryDDE_ONM_all","-qloc personal","-view", "vwDDE_CM_Status2","-vloc project","-identity","WRE*","-format rtf"
-view 
Start-Process -FilePath $cradleBin -ArgumentList $args 
Write-Host "Executable finished. Press any key to exit or continue..."
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null