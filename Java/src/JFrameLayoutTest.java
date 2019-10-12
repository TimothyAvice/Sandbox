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
        JLabel info1 = new JLabel("Info1"); JLabel info2 = new JLabel("Info2");
        JLabel info3 = new JLabel("Info3");
        JButton test = new JButton("Test");
        JButton test2 = new JButton("Test2");
        JButton test3 = new JButton("Test3");
        JButton test4 = new JButton("Test4");
        JButton test5 = new JButton("Test5");

        information.setPreferredSize(new Dimension(getWidth(),40));
        mainPanel.setPreferredSize(new Dimension(1000,800));

        // Setting up the menu bar
        setJMenuBar(menu);
        menu.add(file);menu.add(mode);menu.add(info);
        file.add(save);file.add(load);file.add(print);file.add(exit);
        mode.add(sim);mode.add(build);
        info.add(usage);info.add(help);

        // Adding test components
        information.add(info1); information.add(info2); information.add(info3);
        mainPanel.add(test);
        sideButtons.add(test2);sideButtons.add(test3);sideButtons.add(test4);sideButtons.add(test5);

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

        // Moving shapes


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
