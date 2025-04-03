#include "introwindow.h"
#include "./ui_introwindow.h"

IntroWindow::IntroWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::IntroWindow)
{
    ui->setupUi(this);
}

IntroWindow::~IntroWindow()
{
    delete ui;
}
