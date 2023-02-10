package org.demetrius.util;

import javax.sound.sampled.*;
import java.io.File;
import java.io.IOException;

public class SimpleAudioPlayer {
    Long currentFrame;
    Clip clip;
    String status;
    AudioInputStream audioInputStream;
    String link;


    public SimpleAudioPlayer(String link) throws UnsupportedAudioFileException, IOException, LineUnavailableException {
        this.link = link;
        audioInputStream = AudioSystem.getAudioInputStream(new File(link).getAbsoluteFile());
        clip = AudioSystem.getClip();
        clip.open(audioInputStream);
        clip.loop(0);
    }
    public void play()
    {
        //start the clip
        clip.start();

        status = "play";
    }
    public void stop() throws UnsupportedAudioFileException,
            IOException, LineUnavailableException
    {
        currentFrame = 0L;
        clip.stop();
        clip.close();
    }
}
