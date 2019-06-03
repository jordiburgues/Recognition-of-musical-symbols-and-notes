package com.example.pitchplayer;

import android.content.Context;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;

import java.util.ArrayList;

import de.hdodenhof.circleimageview.CircleImageView;

public class RecyclerViewAdapter extends RecyclerView.Adapter<RecyclerViewAdapter.ViewHolder> {

    private static final String TAG = "RecyclerViewAdapter";
    private ArrayList<String> mImageNames;
    private ArrayList<String> mImages ;
    private Context mContext;

    public RecyclerViewAdapter(ArrayList<String> ImageNames, ArrayList<String> Images, Context context) {
        mImageNames = ImageNames;
        mImages = Images;
        mContext = context;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View view = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.layout_listitem,viewGroup,false);
        ViewHolder holder = new ViewHolder(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder viewHolder, final int i) {
        Log.d(TAG, "onBindViewHolder:called.");

        Glide.with(mContext)
                .asBitmap()
                .load(mImages.get(i))
                .into(viewHolder.mimage);


        viewHolder.imageName.setText(mImageNames.get(i));
        //viewHolder.imageName.setText(String.valueOf(mImages.get(i)));
        viewHolder.parentLayout.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Log.d(TAG,"onClick: clicked on: " + mImageNames.get(i));
                Toast.makeText(mContext,mImageNames.get(i), Toast.LENGTH_SHORT).show();

                Intent intent = new Intent(mContext, GalleryActivity.class);
                intent.putExtra("image_url", mImages.get(i));
                intent.putExtra("image_name", mImageNames.get(i));
                mContext.startActivity(intent);
            }


        });

    }

    @Override
    public int getItemCount() {
        return mImageNames.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{

    ImageView mimage;
    TextView imageName;
    RelativeLayout parentLayout;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            mimage = itemView.findViewById(R.id.image);
            imageName=itemView.findViewById(R.id.im_name);
            parentLayout = itemView.findViewById(R.id.parent_layout);
        }
    }
}

