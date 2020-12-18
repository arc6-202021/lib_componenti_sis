#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))


# -- TEST mux4i8b

# Copia il file blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part2.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part3.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part4.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part5.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part6.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part7.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part8.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part9.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part10.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part11.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part12.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part13.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part14.blif
cp $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part15.blif

mv $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part1.blif

# Genera gli output corretti

python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --endnum 1048576 > $SCRIPTDIR/tests/test_mux4i8b_part1_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 1048576 --endnum 2097152 > $SCRIPTDIR/tests/test_mux4i8b_part2_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 2097152 --endnum 4194304 > $SCRIPTDIR/tests/test_mux4i8b_part3_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 4194304 --endnum 8388608 > $SCRIPTDIR/tests/test_mux4i8b_part4_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 8388608 --endnum 16777216 > $SCRIPTDIR/tests/test_mux4i8b_part5_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 16777216 --endnum 33554432 > $SCRIPTDIR/tests/test_mux4i8b_part6_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 33554432 --endnum 67108864 > $SCRIPTDIR/tests/test_mux4i8b_part7_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 67108864 --endnum 134217728 > $SCRIPTDIR/tests/test_mux4i8b_part8_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 134217728 --endnum 268435456 > $SCRIPTDIR/tests/test_mux4i8b_part9_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 268435456 --endnum 536870912 > $SCRIPTDIR/tests/test_mux4i8b_part10_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 536870912 --endnum 1073741824 > $SCRIPTDIR/tests/test_mux4i8b_part11_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 1073741824 --endnum 2147483648 > $SCRIPTDIR/tests/test_mux4i8b_part12_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 2147483648 --endnum 4294967296 > $SCRIPTDIR/tests/test_mux4i8b_part13_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 4294967296 --endnum 8589934592 > $SCRIPTDIR/tests/test_mux4i8b_part14_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum 8589934592 --endnum 17179869184 > $SCRIPTDIR/tests/test_mux4i8b_part15_correct_output.txt

# Genera gli script di test

python3 $SCRIPTDIR/../test_generator.py 34 --simulate --endnum 1048576 > $SCRIPTDIR/tests/test_mux4i8b_part1.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 1048576 --endnum 2097152 > $SCRIPTDIR/tests/test_mux4i8b_part2.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 2097152 --endnum 4194304 > $SCRIPTDIR/tests/test_mux4i8b_part3.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 4194304 --endnum 8388608 > $SCRIPTDIR/tests/test_mux4i8b_part4.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 8388608 --endnum 16777216 > $SCRIPTDIR/tests/test_mux4i8b_part5.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 16777216 --endnum 33554432 > $SCRIPTDIR/tests/test_mux4i8b_part6.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 33554432 --endnum 67108864 > $SCRIPTDIR/tests/test_mux4i8b_part7.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 67108864 --endnum 134217728 > $SCRIPTDIR/tests/test_mux4i8b_part8.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 134217728 --endnum 268435456 > $SCRIPTDIR/tests/test_mux4i8b_part9.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 268435456 --endnum 536870912 > $SCRIPTDIR/tests/test_mux4i8b_part10.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 536870912 --endnum 1073741824 > $SCRIPTDIR/tests/test_mux4i8b_part11.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 1073741824 --endnum 2147483648 > $SCRIPTDIR/tests/test_mux4i8b_part12.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 2147483648 --endnum 4294967296 > $SCRIPTDIR/tests/test_mux4i8b_part13.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 4294967296 --endnum 8589934592 > $SCRIPTDIR/tests/test_mux4i8b_part14.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum 8589934592 --endnum 17179869184 > $SCRIPTDIR/tests/test_mux4i8b_part15.script
