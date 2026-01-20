# Startup python
c:\code\pyenv\.venv\Scripts\activate.ps1



# Git Command Aliases
Function gits {git  status}
Function gita([String]$name) {git add $name}
Function gitc([String]$message) {git commit -m $message}
Function gitp {git push origin master}
Function glazy([String]$message) {
    git add .;
    #git commit -m "update";
    git commit -m $message;
    git push origin master
}
Set-Alias -Name gs -Value gits -Force
Set-Alias -Name ga -Value gita -Force
Set-Alias -Name gc -Value gitc -Force
Set-Alias -Name gp -Value gitp -Force

#Set alias
Set-Alias -Name log -Value c:\apps\logseq\logseq.exe
Set-Alias -Name np -Value notepad++.exe



Function vi([String]$fn) {nvim $fn}
Function vim([String]$fn) {nvim $fn}
Function jo {notepad++.exe C:\\work\\00_docs\\Journal.md}

Function crg([String]$search_str){clear; rg $search_str}

# Function geo {cd "C:\work\04_Projects\cy26\WPR129649_GEO_BIAS"}


Function windirstat([String]$dirname) {c:\apps\windirstat\WinDirStat.exe $dirname}
Set-Alias -Name wds -Value windirstat -Force

Function co([String]$question) {
    $copilotURL = "https://copilot.microsoft.com";
    Start-Process -FilePath $copilotURL;
    Set-Clipboard -Value $question;
}

function cut {
    param(
        [Parameter(ValueFromPipeline=$True)]
        [string]$inputobject,
        [string]$delimiter='\s+',
        [string[]]$field
    )
    process {
        if ($field -eq $null) {
            $inputobject -split $delimiter
        } else {
            ($inputobject -split $delimiter)[$field]
        }
    }
}

# Install GoLang : winget install GoLang.Go
# Install moor: go install github.com/walles/moor/v2/cmd/moor@latest
Set-Alias -Name less -Value moor
# Use with bat
$env:BAT_PAGER = "moor"

Function blah{
	$INITIAL_QUERY = "${*:-}"
	$RG_PREFIX = "rg --column --line-number --no-heading --color=always --smart-case"
	"" |
	fzf --ansi --disabled --query "$INITIAL_QUERY" `
	  --bind "start:reload:$RG_PREFIX {q}" `
	  --bind "change:reload:sleep 0.1 & $RG_PREFIX {q} || rem" `
	  --bind 'ctrl-s:transform:if not "%FZF_PROMPT%" == "1. ripgrep> " (echo ^rebind^(change^)^+^change-prompt^(1. ripgrep^> ^)^+^disable-search^+^transform-query:echo ^{q^} ^> %TEMP%\rg-fzf-f ^& type %TEMP%\rg-fzf-r) else (echo ^unbind^(change^)^+^change-prompt^(2. fzf^> ^)^+^enable-search^+^transform-query:echo ^{q^} ^> %TEMP%\rg-fzf-r ^& type %TEMP%\rg-fzf-f)' `
	  --color 'hl:-1:underline,hl+:-1:underline:reverse' `
	  --delimiter ':' `
	  --prompt '1. ripgrep> ' `
	  --preview-label 'Preview' `
	  --header 'CTRL-S: Switch between ripgrep/fzf' `
	  --header-first `
	  --preview 'bat --color=always {1} --highlight-line {2} --style=plain' `
	  --preview-window 'up,60%,border-bottom,+{2}+3/3'
}

Function pr{
        $INITIAL_QUERY = "${*:-}"
        $RG_PREFIX = "rg --column --line-number --no-heading --color=always --smart-case"
        "" |
        fzf --ansi --disabled --query "$INITIAL_QUERY" `
          --bind "start:reload:$RG_PREFIX {q}" `
          --bind "change:reload:sleep 0.1 & $RG_PREFIX {q} || rem" `
          --bind 'ctrl-s:transform:if not "%FZF_PROMPT%" == "1. ripgrep> " (echo ^rebind^(change^)^+^change-prompt^(1. ripgrep^> ^)^+^disable-search^+^transform-query:echo ^{q^} ^> %TEMP%\rg-fzf-f ^& type %TEMP%\rg-fzf-r) else (echo ^unbind^(change^)^+^change-prompt^(2. fzf^> ^)^+^enable-search^+^transform-query:echo ^{q^} ^> %TEMP%\rg-fzf-r ^& type %TEMP%\rg-fzf-f)' `
          --color 'hl:-1:underline,hl+:-1:underline:reverse' `
          --delimiter ':' `
          --prompt '1. ripgrep> ' `
          --preview-label 'Preview' `
          --header 'CTRL-S: Switch between ripgrep/fzf' `
          --header-first `
          --preview 'bat --color=always {1} --highlight-line {2}' `
          --preview-window 'right,60%,border-bottom,+{2}+3/3'
}




