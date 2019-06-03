package com.example.pitchplayer;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.Window;
import android.view.WindowManager;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    //vars
    private ArrayList<String> mNames = new ArrayList<>();
    private ArrayList<String> mImageUrls = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_main);
        Log.d(TAG, "onCreate: started. ");
        initImageBitmap();
    }

    private void initImageBitmap(){

        Log.d(TAG, "initImageBitmaps: preparing bitmaps. ");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/8/83/La_La_Land_soundtrack.jpg");
        mNames.add("Another Day of Sun");

        mImageUrls.add("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2cdf274f-a395-4e79-8ebc-ff8a8b8787fa/d4phvpy-195fc70c-622a-404f-96a8-246ba4ff929d.jpg/v1/fill/w_894,h_894,q_70,strp/the_lord_of_the_rings_golden_movie_logo_by_freeco_d4phvpy-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzAwMCIsInBhdGgiOiJcL2ZcLzJjZGYyNzRmLWEzOTUtNGU3OS04ZWJjLWZmOGE4Yjg3ODdmYVwvZDRwaHZweS0xOTVmYzcwYy02MjJhLTQwNGYtOTZhOC0yNDZiYTRmZjkyOWQuanBnIiwid2lkdGgiOiI8PTMwMDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.fnVQv4K6vHZgOBKWRecH-CjgJDWj0IVaxgI1AmhxJTU");
        mNames.add("In Dreams");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/3/33/Up_-_Walt_Disney_Records.jpg");
        mNames.add("Carl and Ellie");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/7/78/Game_of_Thrones_%28season_6_soundtrack%29_cover.jpg");
        mNames.add("Game of Thrones");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/8/83/La_La_Land_soundtrack.jpg");
        mNames.add("Mia and Sebastian");

        mImageUrls.add("https://pixel.nymag.com/imgs/daily/vulture/2016/12/18/18-Star-Wars-Logo.w330.h330.jpg");
        mNames.add("Remember Me");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/8/83/La_La_Land_soundtrack.jpg");
        mNames.add("Finding Nemo");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/8/83/La_La_Land_soundtrack.jpg");
        mNames.add("City of Stars");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/8/83/La_La_Land_soundtrack.jpg");
        mNames.add("Rey's Theme");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/8/83/La_La_Land_soundtrack.jpg");
        mNames.add("Speechless");

        mImageUrls.add("https://upload.wikimedia.org/wikipedia/en/8/83/La_La_Land_soundtrack.jpg");
        mNames.add("Concerning Hobbits");


        initRecyclerView();

    }

    private void initRecyclerView(){
        Log.d(TAG, "initRecyclerView: init recyclerview.");
        RecyclerView recyclerView = findViewById(R.id.recyclerview);
        RecyclerViewAdapter adapter = new RecyclerViewAdapter(mNames,mImageUrls, this);
        //recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(adapter);


    }


}
