$INITIAL_QUERY = "${*:-}"
$RG_PREFIX = "rg --column --line-number --no-heading --color=always --smart-case"
"" |
fzf --ansi --disabled --query "$INITIAL_QUERY" `
  --bind "start:reload:$RG_PREFIX {q}" `
  --bind "change:reload:sleep 0.1 & $RG_PREFIX {q} || rem" `
  --bind 'ctrl-s:transform:if not "%FZF_PROMPT%" == "1. ripgrep> " (echo ^rebind^(change^)^+^change-prompt^(1. ripgrep^> ^)^+^disable-search^+^transform-query:echo ^{q^} ^> %TEMP%\rg-fzf-f ^& type %TEMP%\rg-fzf-r) else (echo ^unbind^(change^)^+^change-prompt^(2. fzf^> ^)^+^enable-search^+^transform-query:echo ^{q^} ^> %TEMP%\rg-fzf-r ^& type %TEMP%\rg-fzf-f)' `
  --bind 'ctrl-o:execute(nvim {1} +{2})' `
  --color 'hl:-1:underline,hl+:-1:underline:reverse' `
  --delimiter ':' `
  --prompt '1. ripgrep> ' `
  --preview-label 'Preview' `
  --header 'CTRL-S: Switch between ripgrep/fzf | CTRL-O: open in vim' `
  --header-first `
  --preview 'bat --color=always {1} --highlight-line {2}' `
  --preview-window 'right,60%,border-bottom,+{2}+3/3'
