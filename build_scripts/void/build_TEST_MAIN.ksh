
export prj_dir='/user/home/jlooper/pb/router_os'

# Do private build
export build_params=$prj_dir'/build_parameters.txt'
private_build -p $build_params 

export build_id='P7.401C'
export build_dir=$prj_dir'/'$build_id
echo $build_dir 
# Create the TEST.exe

export obj=$build_dir'/objects/TEST_ROUTER_MAIN.o'
export exe=$build_dir'/executables_site1/TEST_ROUTER_MAIN.exe'
xlc $obj -o $exe
$exe
