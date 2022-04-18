echo " VERSIONS "
echo " "
#if macos
sw_vers
#if linux
lsb_release -d
echo " "
echo "Compilers and Interpreters"
javac -version
python --version
perl -version | grep 'This is'
cobc -version | grep 'cobc'
fpc -v | grep 'Compiler'
ruby -v
lua -v
awk -version
php -v
echo "GCC"
gcc -v
echo " "
echo "Builders Commandline Tools"
ant -version
make -v | grep 'Make'
xcode-select --version
pip -V
echo " "
echo "Environments"
conda -V
jupyter --version

echo " "
echo "Other Software "
vim -version | grep 'VIM'
echo "sqlite ";  sqlite -version
