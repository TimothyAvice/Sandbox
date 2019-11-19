package Math;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.*;
import java.awt.image.BufferedImage;

public class MandelBrotSet extends JPanel implements ChangeListener {
    public static final int WIDTH = 1000;
    public static final int HEIGHT = 800;
    public static JSlider iterations = new JSlider(JSlider.HORIZONTAL, 0, 200, 100);
    public static JSlider scale = new JSlider(JSlider.VERTICAL, 1, 5000, 200);
    public static JSlider xoffset = new JSlider(JSlider.HORIZONTAL, -10000, 10000, 0);
    public static JSlider yoffset = new JSlider(JSlider.VERTICAL, -10000, 10000, 0);
    public static int ITERATIONS = 100;
    public static int XOFFSET = 0;
    public static int YOFFSET = 0;
    public static float SCALE = 200;

    private BufferedImage buffer;

    MandelBrotSet(){
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        buffer = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);

        // Iteration slider
        iterations.setPaintLabels(true);
        iterations.setPaintTrack(true);
        iterations.setPaintTicks(true);

        iterations.setMajorTickSpacing(100);
        iterations.setMinorTickSpacing(10);

        // Scale slider
        scale.setPaintLabels(true);
        scale.setPaintTrack(true);
        scale.setPaintTicks(true);

        scale.setMajorTickSpacing(1000);
        scale.setMinorTickSpacing(10);

        iterations.addChangeListener(this);
        scale.addChangeListener(this);
        xoffset.addChangeListener(this);
        yoffset.addChangeListener(this);

        // Drawing the set
        renderMandelBrotSet();
        repaint();

        // Setting up the frame
        JFrame jFrame = new JFrame("MandelBrotSet");
        jFrame.setLayout(new BorderLayout());
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jFrame.getContentPane().add(this, BorderLayout.CENTER);
        jFrame.getContentPane().add(iterations, BorderLayout.NORTH);
        jFrame.getContentPane().add(scale, BorderLayout.EAST);
        jFrame.getContentPane().add(xoffset, BorderLayout.SOUTH);
        jFrame.getContentPane().add(yoffset, BorderLayout.WEST);
        jFrame.pack();
        jFrame.setVisible(true);
    }

    @Override
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        g.drawImage(buffer, 0,0,null);
    }

    public void renderMandelBrotSet(){

        for(int x = 0; x < WIDTH; x++){
            for(int y = 0; y < HEIGHT; y++){
                int color = calculatePoint( (x - (WIDTH/2f) + XOFFSET)/SCALE, (y - (HEIGHT/2f) + YOFFSET)/SCALE);

                buffer.setRGB(x,y,color);
            }
        }
    }

    public int calculatePoint(float x, float y){

        float cx = x;
        float cy = y;

        int i = 0;

        for(; i<ITERATIONS; i++){

            float nx = x*x - y*y + cx;
            float ny = 2*x*y + cy;
            x = nx;
            y = ny;

            if(x*x + y*y > 4)
                break;
        }

        if(i==ITERATIONS)
            return 0x00000000;
        return Color.HSBtoRGB((float)i/ITERATIONS, 0.5f, 1);
    }

    public static void main(String[] args) {
        new MandelBrotSet();
    }

    @Override
    public void stateChanged(ChangeEvent changeEvent) {
        ITERATIONS = iterations.getValue();
        SCALE = scale.getValue();
        XOFFSET = xoffset.getValue();
        YOFFSET = yoffset.getValue();
        renderMandelBrotSet();
        repaint();
    }
}
