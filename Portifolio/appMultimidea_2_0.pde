PImage corpo,cranio,costela,pernas,braco_dir,braco_esq;
int x_cranio = 900;
int x_costela = 900;
int y_cranio = 50;
int y_pernas = 400;
int y_costela = 200;
int x_pernas = 600;
int x_bracodir = 600;
int y_bracodir = 50;
int x_bracoesq = 800;
int y_bracoesq = 500;
boolean dragging_cranio,dragging_costela,dragging_bracodir,dragging_bracoesq,dragging_perna = false;


void setup(){
  size(1200,900);
  background(235, 46, 33);
  corpo = loadImage("corpo.png");
  cranio = loadImage("CRANIO.png");
  costela = loadImage("COSTELAS.png");
  pernas = loadImage("PERNAS.png");
  braco_dir = loadImage("BRACO_DIREITO.png");
  braco_esq = loadImage("BRACO_ESQUERDO.png");
}

void draw(){
  if (x_cranio<=260 && x_cranio>=240 && y_cranio<=60 && y_cranio>=40) background(0,255,0);
  else if (x_costela<=260 && x_costela>= 220 && y_costela<=160 && y_costela>=120) background(0,255,0);
  else if (x_bracodir<=200 && x_bracodir>= 170 && y_bracodir<=200 && y_bracodir>=170) background(0,255,0);
  else if (x_bracoesq<=370 && x_bracoesq>=340 && y_bracoesq<=200 && y_bracoesq>=170) background(0,255,0);
  else if (x_pernas<=260 && x_pernas>=220 && y_pernas<=450 && y_pernas>=400) background(0,255,0);
  else background(255,0,0);
  image(corpo,-100,0,800,800);
  image(cranio,x_cranio,y_cranio,100,100);
  image(costela,x_costela,y_costela,140,300);
  image(pernas,x_pernas,y_pernas,150,280);
  image(braco_dir,x_bracodir,y_bracodir,70,270);
  image(braco_esq,x_bracoesq,y_bracoesq,70,270);
}

void mousePressed() {
  // Verificar se o mouse está sobre a imagem
  if (mouseX >= x_cranio && mouseX <= x_cranio + cranio.width && mouseY >= y_cranio && mouseY <= y_cranio + cranio.height) {
    dragging_cranio = true; // Começar a arrastar a imagem
  }else if (mouseX >= x_costela && mouseX <= x_costela + costela.width && mouseY >= y_costela && mouseY <= y_costela + costela.height){
    dragging_costela = true;
  }else if (mouseX >= x_pernas && mouseX <= x_pernas + pernas.width && mouseY >= y_pernas && mouseY <= y_pernas + pernas.height){
    dragging_perna = true;
  }else if (mouseX >= x_bracodir && mouseX <= x_bracodir + braco_dir.width && mouseY >= y_bracodir && mouseY <= y_bracodir + braco_dir.height){
    dragging_bracodir = true;
  }else if (mouseX >= x_bracoesq && mouseX <= x_bracoesq + braco_esq.width && mouseY >= y_bracoesq && mouseY <= y_bracoesq + braco_esq.height){
    dragging_bracoesq = true;
  }
}

void mouseReleased() {
  dragging_cranio = false; // Parar de arrastar a imagem quando o botão do mouse é solto
  dragging_costela = false;
  dragging_bracoesq = false;
  dragging_bracodir = false;
  dragging_perna = false;
}

void mouseDragged() {
  if (dragging_cranio) {
    x_cranio = mouseX - cranio.width/2; 
    y_cranio = mouseY - cranio.height/2; // Atualizar a posição y da imagem durante o arrasto
  }else if (dragging_costela){
    x_costela = mouseX - costela.width/2; 
    y_costela = mouseY - costela.height/2; 
  }else if (dragging_perna){
    x_pernas = mouseX - pernas.width/2; 
    y_pernas = mouseY - pernas.height/2; 
  }else if (dragging_bracodir){
    x_bracodir = mouseX - braco_dir.width/2; 
    y_bracodir = mouseY - braco_dir.height/2; 
  }else if (dragging_bracoesq){
    x_bracoesq = mouseX - braco_esq.width/2; 
    y_bracoesq = mouseY - braco_esq.height/2; 
  }
}
