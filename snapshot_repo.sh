# Change to commit

# Get shortened name for commit
git clone --filter=tree:0 ssh://git@git.faa.gov:7999/waas/m2-dcp.git

# mirror the commit
robocopy "C:\code\m2-dcp" ".\E1_bd8912" /MIR

# rm extra stuff not needed.