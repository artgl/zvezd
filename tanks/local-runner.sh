pushd `dirname $0` > /dev/null
SCRIPTDIR=`pwd`
popd > /dev/null

#java -cp ".;*;$SCRIPTDIR/*;local-runner.jar;/home/art_gl/Downloads/tanks-runner" Run -p2-name=EmptyPlayer true true 1 result.txt true true false &
#java -cp ".:local-runner.jar" Run -base-adapter-port=31000 -debug=true -tick-count=5000 -render-to-screen-scale=0.75 -render-to-screen=true -render-to-screen-sync=true -bunker=true -p1-name=EmptyPlayer -p2-name=EmptyPlayer -results-file=result.txt true true 1 result.txt true true false
java -cp ".:local-runner-new.jar" Run -base-adapter-port=31000 -debug=true -tick-count=5000 -render-to-screen-scale=0.75 -render-to-screen=true -render-to-screen-sync=true -bunker=false -p1-name=first -p2-name=second -results-file=result.txt ""#LocalTestPlayer"" ""#LocalTestPlayer""
#java -cp ".:2" Run true true 1 result.txt true true false
echo $?

