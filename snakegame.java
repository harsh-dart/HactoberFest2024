import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.Random;

public class SnakeGame extends JPanel implements ActionListener {
    private final int WIDTH = 600;
    private final int HEIGHT = 400;
    private final int DOT_SIZE = 10;
    private final int ALL_DOTS = (WIDTH * HEIGHT) / (DOT_SIZE * DOT_SIZE);
    private final int DELAY = 140;

    private final ArrayList<Point> snake = new ArrayList<>();
    private Point food;
    private int direction;
    private boolean running = false;

    public SnakeGame() {
        setBackground(Color.BLACK);
        setFocusable(true);
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                switch (e.getKeyCode()) {
                    case KeyEvent.VK_UP -> direction = 0;
                    case KeyEvent.VK_DOWN -> direction = 1;
                    case KeyEvent.VK_LEFT -> direction = 2;
                    case KeyEvent.VK_RIGHT -> direction = 3;
                }
            }
        });
        startGame();
    }

    private void startGame() {
        running = true;
        snake.clear();
        snake.add(new Point(5, 5));
        direction = 3; // Start moving right
        spawnFood();
        Timer timer = new Timer(DELAY, this);
        timer.start();
    }

    private void spawnFood() {
        Random rand = new Random();
        int x = rand.nextInt(WIDTH / DOT_SIZE);
        int y = rand.nextInt(HEIGHT / DOT_SIZE);
        food = new Point(x, y);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (running) {
            moveSnake();
            checkCollision();
            repaint();
        }
    }

    private void moveSnake() {
        Point head = new Point(snake.get(0));
        switch (direction) {
            case 0 -> head.y--; // Up
            case 1 -> head.y++; // Down
            case 2 -> head.x--; // Left
            case 3 -> head.x++; // Right
        }
        snake.add(0, head);
        if (head.equals(food)) {
            spawnFood(); // Eat food
        } else {
            snake.remove(snake.size() - 1); // Remove tail
        }
    }

    private void checkCollision() {
        Point head = snake.get(0);
        // Check wall collision
        if (head.x < 0 || head.x >= WIDTH / DOT_SIZE || head.y < 0 || head.y >= HEIGHT / DOT_SIZE) {
            running = false;
        }
        // Check self collision
        for (int i = 1; i < snake.size(); i++) {
            if (head.equals(snake.get(i))) {
                running = false;
            }
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (running) {
            g.setColor(Color.RED);
            g.fillRect(food.x * DOT_SIZE, food.y * DOT_SIZE, DOT_SIZE, DOT_SIZE);
            g.setColor(Color.GREEN);
            for (Point p : snake) {
                g.fillRect(p.x * DOT_SIZE, p.y * DOT_SIZE, DOT_SIZE, DOT_SIZE);
            }
        } else {
            showGameOver(g);
        }
    }

    private void showGameOver(Graphics g) {
        g.setColor(Color.WHITE);
        g.drawString("Game Over", WIDTH / 2 - 30, HEIGHT / 2);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Snake Game");
        SnakeGame game = new SnakeGame();
        frame.add(game);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}