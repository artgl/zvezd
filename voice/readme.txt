Install portaudio19-dev

https://www.unicom.com/blog/entry/686

https://cmusphinx.github.io/wiki/pocketsphinx_pronunciation_evaluation/

https://netcologne.dl.sourceforge.net/project/cmusphinx/Acoustic%20and%20Language%20Models/Russian/cmusphinx-ru-5.2.tar.gz

festival --server
echo "пару раз мне чуть процессор не спалили, а в целом житуха ничего" | festival_client --ttw | aplay

alsamixer
sudo alsactl store

DATA=/home/artgl/Projects/2018_voice/downloads/cmusphinx-ru-5.2 && unbuffer pocketsphinx_continuous -backtrace yes -fsgusefiller yes -bestpath no -inmic yes -jsgf $DATA/my.jsgf -dict $DATA/my.dict -hmm $DATA -logfn /dev/stdout | gawk -F'[():-]' '/pocketsphinx/ {if (int($7) < 5300) print $0" "int($7)}'

-beam and -wbeam 

https://makezine.com/projects/use-raspberry-pi-for-voice-control/
