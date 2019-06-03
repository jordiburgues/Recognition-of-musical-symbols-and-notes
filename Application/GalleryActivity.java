package com.example.pitchplayer;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.davemorrissey.labs.subscaleview.ImageSource;
import com.davemorrissey.labs.subscaleview.SubsamplingScaleImageView;

import org.w3c.dom.Text;

public class GalleryActivity extends AppCompatActivity {
    private static final String TAG = "GalleryActivity";
    public static final String CHOICE="com.example.pitchplayer.CHOICE";
    public static final String KEYSIGNATURE="com.example.pitchplayer.KEYSIGNATURE";
    public static final String CLEF="com.example.pitchplayer.CLEF";
    RadioGroup radioGroup;
    RadioGroup radioGroup_2;
    RadioButton radioButton;
    RadioButton radioButton_2;
    String keysignature;
    String clef;

    int selected_choice=0;
    private Button button;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_main);
        setContentView(R.layout.activity_gallery);
        Log.d(TAG, "onCreate: started.");
        final String choice = getIncomingIntent();
        button = (Button) findViewById(R.id.button1);
        radioGroup = findViewById(R.id.radioGroup);
        radioGroup_2=findViewById(R.id.radioGroup_2);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openScore(choice);
            }
        });
    }

    public void openScore(String cscore){
        int radioId = radioGroup.getCheckedRadioButtonId();
        int radioId_2=radioGroup_2.getCheckedRadioButtonId();
        radioButton=findViewById(radioId);
        radioButton_2=findViewById(radioId_2);
        keysignature=String.valueOf(radioButton.getText());
        clef=String.valueOf(radioButton_2.getText());
        Intent intent = new Intent(this, PlayScore.class);
        intent.putExtra(CHOICE,cscore);
        intent.putExtra(KEYSIGNATURE,keysignature);
        intent.putExtra(CLEF,clef);
        startActivity(intent);

    }

    private String getIncomingIntent(){
        String choice="";
        Log.d(TAG, "getIncomingIntent: checking for incoming intetns.");
        if (getIntent().hasExtra("image_url") && getIntent().hasExtra("image_name")){
            String imageUrl = getIntent().getStringExtra("image_url");
            String imageName = getIntent().getStringExtra("image_name");
            choice = setImage(imageUrl, imageName);
        }
        return choice;
    }

    private String setImage(String imageUrl, String imageName){
        Log.d(TAG, "setImage: setting the image and name to widgets.");

        TextView name = findViewById(R.id.image_description);
        name.setText(imageName);
        final SubsamplingScaleImageView imageView = (SubsamplingScaleImageView)findViewById(R.id.scoreExplorer);
        if (imageName.equals("Another Day of Sun")){
           selected_choice=R.drawable.anotherdayofsun;
        } else if (imageName.equals("In Dreams")){
           selected_choice=R.drawable.indreams;
        } else if (imageName.equals("Carl and Ellie")){
            selected_choice=R.drawable.carlandellie;
        } else if (imageName.equals("Game of Thrones")){
            selected_choice=R.drawable.gameofthronesintro;
        } else if (imageName.equals("Mia and Sebastian")){
            selected_choice=R.drawable.miandsebastian;
        } else if (imageName.equals("City of Stars")){
            selected_choice=R.drawable.cityofstars;
        } else if (imageName.equals("Remember Me")){
            selected_choice=R.drawable.coco;
        } else if (imageName.equals("Finding Nemo")){
            selected_choice=R.drawable.nemo;
        } else if (imageName.equals("Rey's Theme")){
            selected_choice=R.drawable.rey;
        } else if (imageName.equals("Speechless")){
            selected_choice=R.drawable.speechless;
        }  else if (imageName.equals("Concerning Hobbits")){
            selected_choice=R.drawable.hobbit;
        }
        imageView.setImage(ImageSource.resource(selected_choice));
        return imageName;

    }

    public void checkButton(View v){
        int radioId = radioGroup.getCheckedRadioButtonId();
        radioButton=findViewById(radioId);
        Toast.makeText(this, "Selected key signature: "+ radioButton.getText(),Toast.LENGTH_SHORT).show();

    }

    public void checkButton_2(View v){
        int radioId_2 = radioGroup_2.getCheckedRadioButtonId();
        radioButton_2=findViewById(radioId_2);
        Toast.makeText(this, "Selected clef: "+ radioButton_2.getText(),Toast.LENGTH_SHORT).show();

    }
}
