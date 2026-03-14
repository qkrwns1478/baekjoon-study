read a
read b
read c
read d
sum=$(($a + $b + $c + $d + 300))
if (( "$sum" <= 1800 ))
then
  echo Yes
else
  echo No
fi