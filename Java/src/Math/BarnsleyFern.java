package Math;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.Random;

public class BarnsleyFern extends JPanel{
    private int dim = 640;
    BufferedImage img;

    private BarnsleyFern(){
        setBackground(Color.WHITE);
        setPreferredSize(new Dimension(dim, dim));
        img = new BufferedImage(dim, dim, BufferedImage.TYPE_INT_ARGB);
        generateFern(dim, dim);
    }

    private void generateFern(int w, int h){
        double x = 0;
        double y = 0;

        for (int i = 0; i < 200000; i++) {
            double tmpx, tmpy;
            double r = Math.random();

            if (r <= 0.01) {
                tmpx = 0;
                tmpy = 0.16 * y;
            } else if (r <= 0.08) {
                tmpx = 0.2 * x - 0.26 * y;
                tmpy = 0.23 * x + 0.22 * y + 1.6;
            } else if (r <= 0.15) {
                tmpx = -0.15 * x + 0.28 * y;
                tmpy = 0.26 * x + 0.24 * y + 0.44;
            } else {
                tmpx = 0.85 * x + 0.04 * y;
                tmpy = -0.04 * x + 0.85 * y + 1.6;
            }
            x = tmpx;
            y = tmpy;
            
            img.setRGB((int) Math.round(w / 2f + x * w / 11),
                    (int) Math.round(h - y * h / 11), 0xFF32CD32);
        }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        g.drawImage(img, 0, 0, null);
    }

    public static void main(String[] args) {
        JFrame f = new JFrame();
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setTitle("Barnsley Fern");
        f.setResizable(false);
        f.add(new BarnsleyFern(), BorderLayout.CENTER);
        f.pack();
        f.setLocationRelativeTo(null);
        f.setVisible(true);
    }
}
