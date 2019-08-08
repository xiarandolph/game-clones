#include <SFML/Graphics.hpp>
#include <vector>

const int GAME_WIDTH = 800;
const int GAME_HEIGHT = 600;
const float SPEED = 3.f;

int main()
{
    sf::RenderWindow window(sf::VideoMode(GAME_WIDTH, GAME_HEIGHT), "Breakout");

    sf::RectangleShape paddle;
    paddle.setSize(sf::Vector2f(70.f, 10.f));
    paddle.setPosition((GAME_WIDTH - paddle.getSize().x)/2, GAME_HEIGHT - 60.f);

    std::vector<sf::RectangleShape> bricks;
    for (int i = 0; i < 60; i++) {
        sf::RectangleShape brick;
        brick.setSize(sf::Vector2f(40.f, 20.f));
        brick.setPosition((i % 20) * 40.f, 50 + 21*(i/20));
        // replace with textures later b/c outline goes outside size of brick
        brick.setOutlineColor(sf::Color::Black);
        brick.setOutlineThickness(0.5f);
        bricks.push_back(brick);
    }

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            window.close();
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::A))
            paddle.move(-SPEED, 0);
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::D))
            paddle.move(SPEED, 0);

        // bounds checking
        sf::Vector2f pos = paddle.getPosition();
        if (pos.x < 0)
            paddle.setPosition(0, pos.y);
        else if (pos.x > GAME_WIDTH - paddle.getSize().x)
            paddle.setPosition(GAME_WIDTH - paddle.getSize().x, pos.y);

        window.clear(sf::Color::Black);

        window.draw(paddle);
        for (sf::RectangleShape brick : bricks)
        window.draw(brick);

        window.display();
    }

    return 0;
}