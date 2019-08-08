#include <SFML/Graphics.hpp>

int main()
{
  sf::Window window(sf::VideoMode(800, 600, 32), "Breakout");

  // run the program as long as the window is open
  while (window.isOpen())
  {
    sf::Event event;
    while (window.pollEvent(event))
    {
      // "close requested" event: we close the window
      if (event.type == sf::Event::Closed)
        window.close();
    }
    window.display();
  }

  return 0;
}