#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# -- TEST mux4i8b

randport1=$(python3 -S -c "import random; print(random.randint(0,      40000) * 85899)")
randport2=$(python3 -S -c "import random; print(random.randint(40000,  80000) * 85899)")
randport3=$(python3 -S -c "import random; print(random.randint(80000,  120000) * 85899)")
randport4=$(python3 -S -c "import random; print(random.randint(120000, 160000) * 85899)")
randport5=$(python3 -S -c "import random; print(random.randint(160000, 200000) * 85899)")

# Copia il file blif
mv $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part1.blif
cp $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b_part2.blif
cp $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b_part3.blif
cp $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b_part4.blif
cp $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b_part5.blif

# Genera gli output corretti

python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport1 --endnum $(( randport1 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part1_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport2 --endnum $(( randport2 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part2_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport3 --endnum $(( randport3 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part3_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport4 --endnum $(( randport4 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part4_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport5 --endnum $(( randport5 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part5_correct_output.txt

# Genera gli script di test

python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport1 --endnum $(( randport1 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part1.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport2 --endnum $(( randport2 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part2.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport3 --endnum $(( randport3 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part3.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport4 --endnum $(( randport4 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part4.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport5 --endnum $(( randport5 + 85899 )) > $SCRIPTDIR/tests/test_mux4i8b_part5.script
