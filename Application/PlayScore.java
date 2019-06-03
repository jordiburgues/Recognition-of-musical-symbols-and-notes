package com.example.pitchplayer;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.graphics.PointF;
import android.media.AudioAttributes;
import android.media.AudioManager;
import android.media.SoundPool;
import android.os.CountDownTimer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.GestureDetector;
import android.view.MotionEvent;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.TextView;

import com.davemorrissey.labs.subscaleview.ImageSource;
import com.davemorrissey.labs.subscaleview.SubsamplingScaleImageView;

public class PlayScore extends AppCompatActivity {

    TextView txt;
    public SoundPool soundPool;
    public int note1,note2,note3,note4,note5,note6,note7,note8,note9,note10,note11,note12,note13,note14,note15,note16,note17,note18,note19,note20, note23,note7b, note9b,note12b, note13b,note14b,note21b, note22b,note3b,note6b,note2b,note5b;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_main);
        setContentView(R.layout.activity_play_score);

        Intent intent = getIntent();
        final String choice = intent.getStringExtra(GalleryActivity.CHOICE);
        final String keysignature = intent.getStringExtra(GalleryActivity.KEYSIGNATURE);
        final String clef = intent.getStringExtra(GalleryActivity.CLEF);
        int selected_choice=0;
        int selected_choice_2=0;

        AudioAttributes audioAttributes = new AudioAttributes.Builder()
                .setUsage(AudioAttributes.USAGE_ASSISTANCE_SONIFICATION)
                .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
                .build();

        soundPool = new SoundPool.Builder()
                .setMaxStreams(6)
                .setAudioAttributes(audioAttributes)
                .build();


        //Normal notes
        note1 = soundPool.load(this, R.raw.c42,1);
        note2 = soundPool.load(this, R.raw.d4_2,1);
        note3 = soundPool.load(this, R.raw.e4_2,1);
        note4 = soundPool.load(this, R.raw.f4_2,1);
        note5 = soundPool.load(this, R.raw.g4_2,1);
        note6 = soundPool.load(this, R.raw.a4_2,1);
        note7 = soundPool.load(this, R.raw.b4_2,1);
        note8 = soundPool.load(this, R.raw.c5_2,1);
        note9 = soundPool.load(this, R.raw.d5_2,1);
        note10 = soundPool.load(this, R.raw.e5_2,1);
        note11 = soundPool.load(this, R.raw.f5_2,1);
        note12 = soundPool.load(this, R.raw.g5_2,1);
        note13 = soundPool.load(this, R.raw.a5_2,1);
        note14 = soundPool.load(this, R.raw.b5_2,1);
        note15 = soundPool.load(this, R.raw.c6_2,1);
        note16 = soundPool.load(this, R.raw.d6_2,1);
        note17 = soundPool.load(this, R.raw.e6_2,1);
        note18 = soundPool.load(this, R.raw.f6_2,1);
        note19 = soundPool.load(this, R.raw.g6_2,1);
        note20 = soundPool.load(this, R.raw.a6_2,1);
        note23 = soundPool.load(this, R.raw.g3_2,1);

        //Altered notes (sharps and flats)
        note2b = soundPool.load(this, R.raw.db4_2,1);
        note3b = soundPool.load(this, R.raw.eb4_2,1);
        note5b = soundPool.load(this, R.raw.gb4_2,1);
        note6b = soundPool.load(this, R.raw.ab4_2,1);
        note7b = soundPool.load(this, R.raw.bb4_2,1);
        note9b = soundPool.load(this, R.raw.db5_2,1);
        note12b = soundPool.load(this, R.raw.gb5_2,1);
        note13b = soundPool.load(this, R.raw.ab5_2,1);
        note14b = soundPool.load(this, R.raw.bb5_2,1);
        note21b = soundPool.load(this, R.raw.bb3_2,1);
        note22b = soundPool.load(this, R.raw.ab3_2,1);


        if (choice.equals("Another Day of Sun")){
            selected_choice=R.drawable.anotherdayofsuncolored;
        } else if (choice.equals("In Dreams")){
            selected_choice=R.drawable.indreamscolored;
        } else if (choice.equals("Carl and Ellie")){
            selected_choice=R.drawable.carlandelliecolored;
        } else if (choice.equals("Game of Thrones")){
            selected_choice=R.drawable.gameofthronesintrocolored;
        } else if (choice.equals("Mia and Sebastian")){
            selected_choice=R.drawable.miaseb1colored;
        } else if (choice.equals("City of Stars")){
            selected_choice=R.drawable.cityofstarscolored;
        } else if (choice.equals("Remember Me")){
            selected_choice=R.drawable.cococolored;
        } else if (choice.equals("Finding Nemo")){
            selected_choice=R.drawable.nemocolored;
        } else if (choice.equals("Rey's Theme")){
            selected_choice=R.drawable.reycolored;
        } else if (choice.equals("Speechless")){
            selected_choice=R.drawable.speechlesscolored;
        } else if (choice.equals("Concerning Hobbits")){
            selected_choice=R.drawable.hobbitcolored;
        }

        final Bitmap coloredim = BitmapFactory.decodeResource(getResources(),selected_choice);
        final SubsamplingScaleImageView imageView = (SubsamplingScaleImageView)findViewById(R.id.imageView);

        if (choice.equals("Another Day of Sun")){
            //imageView.setImage(ImageSource.resource(R.drawable.newlalalandresized));
            selected_choice_2=R.drawable.anotherdayofsun;
        } else if (choice.equals("In Dreams")){
            //imageView.setImage(ImageSource.resource(R.drawable.lordoftheringsresized));
            selected_choice_2=R.drawable.indreams;
        } else if (choice.equals("Carl and Ellie")){
            selected_choice_2=R.drawable.carlandellie;
        } else if (choice.equals("Game of Thrones")){
            selected_choice_2=R.drawable.gameofthronesintro;
        } else if (choice.equals("Mia and Sebastian")){
            selected_choice_2=R.drawable.miaseb1resized;
        } else if (choice.equals("City of Stars")){
            selected_choice_2=R.drawable.cityofstars;
        } else if (choice.equals("Remember Me")){
            selected_choice_2=R.drawable.coco;
        } else if (choice.equals("Finding Nemo")){
            selected_choice_2=R.drawable.nemo;
        } else if (choice.equals("Rey's Theme")){
            selected_choice_2=R.drawable.rey;
        } else if (choice.equals("Speechless")){
            selected_choice_2=R.drawable.speechless;
        } else if (choice.equals("Concerning Hobbits")){
            selected_choice_2=R.drawable.hobbit;
        }



        //imageView.setImage(ImageSource.resource(R.drawable.newlalalandresized));
        imageView.setImage(ImageSource.resource(selected_choice_2));


        final GestureDetector gestureDetector = new GestureDetector(this, new GestureDetector.SimpleOnGestureListener() {
            //@Override
            public boolean onDown(MotionEvent e) {
                if (imageView.isReady()) {
                    //Get coordinates of touch event relative to the image
                    PointF sCoord = imageView.viewToSourceCoord(e.getX(), e.getY());
                    float point_x = sCoord.x;
                    float point_y = sCoord.y;

                    //Get R value for the touch event in the color map
                    int pixel = coloredim.getPixel(Math.round(point_x), Math.round(point_y));
                    int r = Color.red(pixel);

                    switch (clef){
                        case "F clef":
                            switch (r){
                                case 60:
                                    switch(keysignature){
                                        case "D major/B minor":
                                            soundPool.play(note2, 1,1,0,0,1);
                                            break;
                                    }
                                    break;
                                case 100:
                                    switch(keysignature){
                                        case "D major/B minor":
                                            soundPool.play(note6, 1,1,0,0,1);
                                            break;
                                    }
                                    break;
                                case 130:
                                    switch(keysignature){
                                        case "D major/B minor":
                                            soundPool.play(note9, 1,1,0,0,1);
                                            break;
                                    }
                                    break;

                            }
                            break;
                        case "G clef":

                            if (r==1) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") || keysignature.equals("D major/B minor")){
                                    soundPool.play(note2b, 1,1,0,0,1);
                                } else if (keysignature.equals("Eb major/C minor") || keysignature.equals("C major/A minor")|| keysignature.equals("F major/D minor")){
                                    soundPool.play(note1, 1,1,0,0,1);
                                }
                            } else if (r==10) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") || keysignature.equals("Eb major/C minor") || keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor") || keysignature.equals("D major/B minor")){
                                    soundPool.play(note2, 1,1,0,0,1);
                                }

                            } else if (r==20) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") || keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor") || keysignature.equals("D major/B minor")){
                                    soundPool.play(note3, 1,1,0,0,1);
                                }  else if (keysignature.equals("Eb major/C minor")){
                                    soundPool.play(note3b, 1,1,0,0,1);
                                }

                            } else if (r==30) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") || keysignature.equals("D major/B minor")){
                                    soundPool.play(note5b, 1,1,0,0,1);
                                }  else if (keysignature.equals("Eb major/C minor") || keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor")){
                                    soundPool.play(note4, 1,1,0,0,1);
                                }
                            } else if (r==40) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor")){
                                    soundPool.play(note6b, 1,1,0,0,1);
                                }  else if (keysignature.equals("Eb major/C minor") || keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor") || keysignature.equals("D major/B minor")){
                                    soundPool.play(note5, 1,1,0,0,1);
                                }

                            } else if (r==50) {
                                Log.v("Apretat","nota");
                                //soundPool.play(note10, 1,1,0,0,1);
                                if (keysignature.equals("A major/F# minor")|| keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor") ||keysignature.equals("D major/B minor")){
                                    soundPool.play(note6, 1,1,0,0,1);
                                } else if (keysignature.equals("Eb major/C minor")){
                                    soundPool.play(note6b, 1,1,0,0,1);
                                }

                            } else if (r==60) {
                                Log.v("Apretat","nota");
                                //soundPool.play(note12, 1,1,0,0,1);
                                if (keysignature.equals("A major/F# minor")|| keysignature.equals("C major/A minor") || keysignature.equals("D major/B minor")){
                                    soundPool.play(note7, 1,1,0,0,1);
                                }  else if (keysignature.equals("Eb major/C minor") || keysignature.equals("F major/D minor") ){
                                    soundPool.play(note7b, 1,1,0,0,1);
                                }
                            } else if (r==70) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") ||keysignature.equals("D major/B minor")){
                                    soundPool.play(note9b, 1,1,0,0,1);
                                }  else if (keysignature.equals("Eb major/C minor")|| keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor")){
                                    soundPool.play(note8, 1,1,0,0,1);
                                }
                            } else if (r==80) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") || keysignature.equals("C major/A minor") || keysignature.equals("Eb major/C minor") || keysignature.equals("F major/D minor") || keysignature.equals("D major/B minor")){
                                    soundPool.play(note9, 1,1,0,0,1);
                                }

                            } else if (r==90) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") || keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor") ||keysignature.equals("D major/B minor" )){
                                    soundPool.play(note10, 1,1,0,0,1);
                                }

                            } else if (r==100) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") || keysignature.equals("D major/B minor")){
                                    soundPool.play(note12b, 1,1,0,0,1);
                                }  else if (keysignature.equals("Eb major/C minor")|| keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor") ){
                                    soundPool.play(note11, 1,1,0,0,1);
                                }

                            } else if (r==110) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("A major/F# minor") ||keysignature.equals("D major/B minor")){
                                    soundPool.play(note13b, 1,1,0,0,1);
                                }  else if (keysignature.equals("Eb major/C minor")|| keysignature.equals("C major/A minor") || keysignature.equals("F major/D minor")){
                                    soundPool.play(note12, 1,1,0,0,1);
                                }

                            } else if (r==120) {
                                Log.v("Apretat","nota");
                                soundPool.play(note13, 1,1,0,0,1);

                            } else if (r==130) {
                                Log.v("Apretat","nota");
                                if (keysignature.equals("F major/D minor")){
                                    soundPool.play(note14b, 1,1,0,0,1);
                                } else
                                    soundPool.play(note14, 1,1,0,0,1);

                            } else if (r==140) {
                                Log.v("Apretat","nota");
                                soundPool.play(note15, 1,1,0,0,1);

                            } else if (r==150) {
                                Log.v("Apretat","nota");
                                soundPool.play(note16, 1,1,0,0,1);

                            } else if (r==160) {
                                Log.v("Apretat","nota");
                                soundPool.play(note17, 1,1,0,0,1);

                            } else if (r==170) {
                                Log.v("Apretat","nota");
                                soundPool.play(note18, 1,1,0,0,1);

                            } else if (r==180){
                                Log.v("Apretat","nota");
                                soundPool.play(note19, 1,1,0,0,1);

                            } else if (r==190) {
                                Log.v("Apretat","nota");
                                soundPool.play(note20, 1,1,0,0,1);

                            } else if (r==200) {
                                Log.v("Apretat","nota");
                                soundPool.play(note21b, 1,1,0,0,1);
                            } else if (r==210) {
                                Log.v("Apretat","nota");
                                soundPool.play(note22b, 1,1,0,0,1);
                            } else if (r==220) {
                                Log.v("Apretat","nota");
                                soundPool.play(note23, 1,1,0,0,1);
                            } else if (r==230) {

                            } else if (r==240) {

                            } else if (r==250) {

                            } else if (r==251) {

                            }

                            break;
                    }




                    //txt.setText(String.valueOf(size));
                }
                return true;
            }
        });


        imageView.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                //float screenX = motionEvent.getX();
                //float screenY = motionEvent.getY();
                //txt.setText(String.valueOf(screenX)+"\n"+String.valueOf(screenY)+"\n");
                return gestureDetector.onTouchEvent(motionEvent);
            }
        });


    }
}
