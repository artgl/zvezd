while [[ `xdotool search Run | xargs -I{} xdotool getwindowgeometry {} | grep "960x600" | wc -l` -lt 2 ]]; do
  ps ax | grep local-runner-new.jar | awk '{print $1}' | xargs -I{} kill {};
  nohup java -cp ".:local-runner-new.jar" Run -base-adapter-port=31000 -debug=true -tick-count=5000 -render-to-screen-scale=0.75 -render-to-screen=true -render-to-screen-sync=true -bunker=true -p1-name=first -p2-name=second -results-file=result.txt ""#LocalTestPlayer"" ""#LocalTestPlayer"" &
  sleep 1.7
done
