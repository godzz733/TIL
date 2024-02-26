void main() {
  playComputerGame();
}

Future<void> playComputerGame() async {
  startBoot();
  await startInternet();
  startGame();
}

void startBoot() {
  print('1. boot Comleted');
}

Future<void> startInternet() async {
  await Future.delayed(Duration(seconds: 3), () {
    print('2. Internet Comleted');
  });
  print('delay completed');
}

void startGame() {
  print('3. Game Comleted');
}
