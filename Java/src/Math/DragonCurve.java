package Math;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DragonCurve extends JFrame {

    private List<Integer> turns;
    private double startingAngle, side;
    private static JSlider iterations = new JSlider(JSlider.HORIZONTAL, 1,16,5);
    private int iter = 5;

    private DragonCurve() {
        super("Dragon Curve");
        setVisible(true);
        setLayout(new BorderLayout());
        add(iterations, BorderLayout.NORTH);
        setBounds(100, 100, 800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        turns = getSequence(iter);
        startingAngle = -iter * (Math.PI / 4);
        side = 400 / Math.pow(2, iter / 2.);

        iterations.setPaintLabels(true);
        iterations.setPaintTicks(true);
        iterations.setPaintTrack(true);

        iterations.setMajorTickSpacing(5);
        iterations.setMinorTickSpacing(1);

        iterations.addChangeListener(changeEvent -> {
            iter = iterations.getValue();
            turns = getSequence(iter);
            startingAngle = -iter * (Math.PI / 4);
            side = 400 / Math.pow(2, iter / 2.);
            repaint();
        });
    }

    private List<Integer> getSequence(int iterations) {
        List<Integer> turnSequence = new ArrayList<Integer>();
        for (int i = 0; i < iterations; i++) {
            List<Integer> copy = new ArrayList<Integer>(turnSequence);
            Collections.reverse(copy);
            turnSequence.add(1);
            for (Integer turn : copy) {
                turnSequence.add(-turn);
            }
        }
        return turnSequence;
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.setColor(Color.BLACK);
        double angle = startingAngle;
        int x1 = 230, y1 = 350;
        int x2 = x1 + (int) (Math.cos(angle) * side);
        int y2 = y1 + (int) (Math.sin(angle) * side);
        g.drawLine(x1, y1, x2, y2);
        x1 = x2;
        y1 = y2;
        for (Integer turn : turns) {
            angle += turn * (Math.PI / 2);
            x2 = x1 + (int) (Math.cos(angle) * side);
            y2 = y1 + (int) (Math.sin(angle) * side);
            g.drawLine(x1, y1, x2, y2);
            x1 = x2;
            y1 = y2;
        }
    }

    public static void main(String[] args) {
        new DragonCurve();
    }
}
