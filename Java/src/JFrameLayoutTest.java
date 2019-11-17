import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;

public class JFrameLayoutTest extends JFrame {
    // Menu Bar components
    JMenuBar menu = new JMenuBar();
    JMenu file = new JMenu("File");
    JMenu mode = new JMenu("Mode");
    JMenu info = new JMenu("Information");
    // File menu
    JMenuItem save = new JMenuItem("Save");
    JMenuItem load = new JMenuItem("Load");
    JMenuItem print = new JMenuItem("Print");
    JMenuItem exit = new JMenuItem("Exit");
    // Mode menu
    JMenuItem sim = new JMenuItem("Simulation");
    JMenuItem build = new JMenuItem("Builder");
    // Information menu
    JMenuItem usage = new JMenuItem("How to use");
    JMenuItem help = new JMenuItem("Help");

    private JFrameLayoutTest() throws HeadlessException {
        // Framework
        super("Layout test");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
        setLayout(new BorderLayout());
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new GridLayout(0,1));
        JPanel information = new JPanel(new GridLayout(0,3));
        JPanel sideButtons = new JPanel(new GridLayout(0,1));

        // Test components
        JLabel ballCountLabel = new JLabel("Balls: "); JLabel speedLabel = new JLabel("Speed (s): ");
        JLabel frameRate = new JLabel("Frame rate: ");
        JButton test = new JButton("Test");
        JButton addBall = new JButton("Add Ball");
        JButton clearAll = new JButton("Clear Frame");
        JButton increaseSpeed = new JButton("|+| Speed");
        JButton decreaseSpeed = new JButton("|-| Speed");

        information.setPreferredSize(new Dimension(getWidth(),40));
        mainPanel.setPreferredSize(new Dimension(1000,800));

        // Setting up the menu bar
        setJMenuBar(menu);
        menu.add(file);menu.add(mode);menu.add(info);
        file.add(save);file.add(load);file.add(print);file.add(exit);
        mode.add(sim);mode.add(build);
        info.add(usage);info.add(help);

        // Adding test components
        information.add(ballCountLabel); information.add(speedLabel); information.add(frameRate);
        mainPanel.add(test);
        sideButtons.add(addBall);sideButtons.add(clearAll);sideButtons.add(increaseSpeed);sideButtons.add(decreaseSpeed);

        add(mainPanel, BorderLayout.CENTER);
        add(information, BorderLayout.SOUTH);
        add(sideButtons, BorderLayout.EAST);

        // Handling how to use
        usage.addActionListener(actionEvent -> {
            try {
                howToUse();
            } catch (IOException e) {
                System.exit(0);
            }
        });

        // Handling help
        help.addActionListener(actionEvent -> {
            try {
                help();
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        // Moving balls


        pack();
    }

    private void howToUse() throws IOException {
        Desktop.getDesktop().open(new File(".\\Java\\src\\about.txt"));
    }

    private void help() throws IOException {
        Desktop.getDesktop().open(new File(".\\Java\\src\\help.txt"));
    }

    public static void main(String[] args) {
        new JFrameLayoutTest();
    }
}
