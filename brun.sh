
python3 one.py
exit

set -e

folder=".build"
Projekt="${PWD##*/}"
clear
#echo "First parameter: $1"
#echo "2nd Parameter: $2"

# docker run -d -p 80:8000 whale

#cd app/src/main
#.desktop/SpaceInvaders ] && rm .desktop/SpaceInvaders

rm -f "${folder}/${Projekt}" > /dev/null

cmake -B "${folder}" -D DESKTOP="" -DCMAKE_BUILD_TYPE=
#$2

#rm -f SpaceIn > /dev/null

cd "${folder}"
make;

cp ${Projekt} ../${Projekt}; cd ..
./${Projekt}

