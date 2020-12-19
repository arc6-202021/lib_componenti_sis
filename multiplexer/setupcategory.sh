#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# -- TEST mux4i8b

randport1=$(python3 -S -c "import random; print(random.randint(0,      40000) * 85899)")
randport2=$(python3 -S -c "import random; print(random.randint(40000,  80000) * 85899)")
randport3=$(python3 -S -c "import random; print(random.randint(80000,  120000) * 85899)")
randport4=$(python3 -S -c "import random; print(random.randint(120000, 160000) * 85899)")
randport5=$(python3 -S -c "import random; print(random.randint(160000, 200000) * 85899)")

randport1_end=$(( randport1 + 85899 ))
randport2_end=$(( randport2 + 85899 ))
randport3_end=$(( randport3 + 85899 ))
randport4_end=$(( randport4 + 85899 ))
randport5_end=$(( randport5 + 85899 ))

if [ "$randport1_end" -lt "0" ]; then
    randport1_end=18446744073709551614
fi

if [ "$randport2_end" -lt "0" ]; then
    randport2_end=18446744073709551614
fi

if [ "$randport3_end" -lt "0" ]; then
    randport3_end=18446744073709551614
fi

if [ "$randport4_end" -lt "0" ]; then
    randport4_end=18446744073709551614
fi

if [ "$randport5_end" -lt "0" ]; then
    randport5_end=18446744073709551614
fi

# Copia il file blif
mv $SCRIPTDIR/mux4i8b.blif $SCRIPTDIR/mux4i8b_part1.blif
cp $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b_part2.blif
cp $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b_part3.blif
cp $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b_part4.blif
cp $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b_part5.blif

# Genera gli output corretti

python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport1 --endnum $randport1_end > $SCRIPTDIR/tests/test_mux4i8b_part1_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport2 --endnum $randport2_end > $SCRIPTDIR/tests/test_mux4i8b_part2_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport3 --endnum $randport3_end > $SCRIPTDIR/tests/test_mux4i8b_part3_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport4 --endnum $randport4_end > $SCRIPTDIR/tests/test_mux4i8b_part4_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 34 --ninputs 4 --mux --startnum $randport5 --endnum $randport5_end > $SCRIPTDIR/tests/test_mux4i8b_part5_correct_output.txt

# Genera gli script di test

python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport1 --endnum $randport1_end > $SCRIPTDIR/tests/test_mux4i8b_part1.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport2 --endnum $randport2_end > $SCRIPTDIR/tests/test_mux4i8b_part2.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport3 --endnum $randport3_end > $SCRIPTDIR/tests/test_mux4i8b_part3.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport4 --endnum $randport4_end > $SCRIPTDIR/tests/test_mux4i8b_part4.script
python3 $SCRIPTDIR/../test_generator.py 34 --simulate --startnum $randport5 --endnum $randport5_end > $SCRIPTDIR/tests/test_mux4i8b_part5.script


# -- TEST mux8i4b

randport1=$(python3 -S -c "import random; print(random.randint(0,      40000) * 171798)")
randport2=$(python3 -S -c "import random; print(random.randint(40000,  80000) * 171798)")
randport3=$(python3 -S -c "import random; print(random.randint(80000,  120000) * 171798)")
randport4=$(python3 -S -c "import random; print(random.randint(120000, 160000) * 171798)")
randport5=$(python3 -S -c "import random; print(random.randint(160000, 200000) * 171798)")

randport1_end=$(( randport1 + 171798 ))
randport2_end=$(( randport2 + 171798 ))
randport3_end=$(( randport3 + 171798 ))
randport4_end=$(( randport4 + 171798 ))
randport5_end=$(( randport5 + 171798 ))

if [ "$randport1_end" -lt "0" ]; then
    randport1_end=18446744073709551614
fi

if [ "$randport2_end" -lt "0" ]; then
    randport2_end=18446744073709551614
fi

if [ "$randport3_end" -lt "0" ]; then
    randport3_end=18446744073709551614
fi

if [ "$randport4_end" -lt "0" ]; then
    randport4_end=18446744073709551614
fi

if [ "$randport5_end" -lt "0" ]; then
    randport5_end=18446744073709551614
fi

# Copia il file blif
mv $SCRIPTDIR/mux8i4b.blif $SCRIPTDIR/mux8i4b_part1.blif
cp $SCRIPTDIR/mux8i4b_part1.blif $SCRIPTDIR/mux8i4b_part2.blif
cp $SCRIPTDIR/mux8i4b_part1.blif $SCRIPTDIR/mux8i4b_part3.blif
cp $SCRIPTDIR/mux8i4b_part1.blif $SCRIPTDIR/mux8i4b_part4.blif
cp $SCRIPTDIR/mux8i4b_part1.blif $SCRIPTDIR/mux8i4b_part5.blif

# Genera gli output corretti

python3 $SCRIPTDIR/../test_generator.py 35 --ninputs 8 --mux --startnum $randport1 --endnum $randport1_end > $SCRIPTDIR/tests/test_mux8i4b_part1_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 35 --ninputs 8 --mux --startnum $randport2 --endnum $randport2_end > $SCRIPTDIR/tests/test_mux8i4b_part2_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 35 --ninputs 8 --mux --startnum $randport3 --endnum $randport3_end > $SCRIPTDIR/tests/test_mux8i4b_part3_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 35 --ninputs 8 --mux --startnum $randport4 --endnum $randport4_end > $SCRIPTDIR/tests/test_mux8i4b_part4_correct_output.txt
python3 $SCRIPTDIR/../test_generator.py 35 --ninputs 8 --mux --startnum $randport5 --endnum $randport5_end > $SCRIPTDIR/tests/test_mux8i4b_part5_correct_output.txt

# Genera gli script di test

python3 $SCRIPTDIR/../test_generator.py 35 --simulate --startnum $randport1 --endnum $randport1_end > $SCRIPTDIR/tests/test_mux8i4b_part1.script
python3 $SCRIPTDIR/../test_generator.py 35 --simulate --startnum $randport2 --endnum $randport2_end > $SCRIPTDIR/tests/test_mux8i4b_part2.script
python3 $SCRIPTDIR/../test_generator.py 35 --simulate --startnum $randport3 --endnum $randport3_end > $SCRIPTDIR/tests/test_mux8i4b_part3.script
python3 $SCRIPTDIR/../test_generator.py 35 --simulate --startnum $randport4 --endnum $randport4_end > $SCRIPTDIR/tests/test_mux8i4b_part4.script
python3 $SCRIPTDIR/../test_generator.py 35 --simulate --startnum $randport5 --endnum $randport5_end > $SCRIPTDIR/tests/test_mux8i4b_part5.script


# -- TEST mux8i8b

#randport1=$(python3 -S -c "import random; print(random.randint(0,   40) * 737869762948381)")
#randport2=$(python3 -S -c "import random; print(random.randint(40,  80) * 737869762948381)")
#randport3=$(python3 -S -c "import random; print(random.randint(80,  120) * 737869762948381)")
#randport4=$(python3 -S -c "import random; print(random.randint(120, 160) * 737869762948381)")
#randport5=$(python3 -S -c "import random; print(random.randint(160, 200) * 737869762948381)")

#randport1_end=$(( randport1 + 42949 ))
#randport2_end=$(( randport2 + 42949 ))
#randport3_end=$(( randport3 + 42949 ))
#randport4_end=$(( randport4 + 42949 ))
#randport5_end=$(( randport5 + 42949 ))

#if [ "$randport1_end" -lt "0" ]; then
#    randport1_end=18446744073709551614
#fi

#if [ "$randport2_end" -lt "0" ]; then
#    randport2_end=18446744073709551614
#fi

#if [ "$randport3_end" -lt "0" ]; then
#    randport3_end=18446744073709551614
#fi

#if [ "$randport4_end" -lt "0" ]; then
#    randport4_end=18446744073709551614
#fi

#if [ "$randport5_end" -lt "0" ]; then
#    randport5_end=18446744073709551614
#fi

# Copia il file blif
#mv $SCRIPTDIR/mux8i8b.blif $SCRIPTDIR/mux8i8b_part1.blif
#cp $SCRIPTDIR/mux8i8b_part1.blif $SCRIPTDIR/mux8i8b_part2.blif
#cp $SCRIPTDIR/mux8i8b_part1.blif $SCRIPTDIR/mux8i8b_part3.blif
#cp $SCRIPTDIR/mux8i8b_part1.blif $SCRIPTDIR/mux8i8b_part4.blif
#cp $SCRIPTDIR/mux8i8b_part1.blif $SCRIPTDIR/mux8i8b_part5.blif

# Genera gli output corretti

#python3 $SCRIPTDIR/../test_generator.py 67 --ninputs 8 --mux --startnum ${randport1}000 --endnum ${randport1_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part1_correct_output.txt
#python3 $SCRIPTDIR/../test_generator.py 67 --ninputs 8 --mux --startnum ${randport2}000 --endnum ${randport2_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part2_correct_output.txt
#python3 $SCRIPTDIR/../test_generator.py 67 --ninputs 8 --mux --startnum ${randport3}000 --endnum ${randport3_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part3_correct_output.txt
#python3 $SCRIPTDIR/../test_generator.py 67 --ninputs 8 --mux --startnum ${randport4}000 --endnum ${randport4_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part4_correct_output.txt
#python3 $SCRIPTDIR/../test_generator.py 67 --ninputs 8 --mux --startnum ${randport5}000 --endnum ${randport5_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part5_correct_output.txt

# Genera gli script di test

#python3 $SCRIPTDIR/../test_generator.py 67 --simulate --startnum ${randport1}000 --endnum ${randport1_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part1.script
#python3 $SCRIPTDIR/../test_generator.py 67 --simulate --startnum ${randport2}000 --endnum ${randport2_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part2.script
#python3 $SCRIPTDIR/../test_generator.py 67 --simulate --startnum ${randport3}000 --endnum ${randport3_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part3.script
#python3 $SCRIPTDIR/../test_generator.py 67 --simulate --startnum ${randport4}000 --endnum ${randport4_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part4.script
#python3 $SCRIPTDIR/../test_generator.py 67 --simulate --startnum ${randport5}000 --endnum ${randport5_end}000 > $SCRIPTDIR/tests/test_mux8i8b_part5.script