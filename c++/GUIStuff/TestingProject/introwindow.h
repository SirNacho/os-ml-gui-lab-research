#ifndef INTROWINDOW_H
#define INTROWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class IntroWindow;
}
QT_END_NAMESPACE

class IntroWindow : public QMainWindow
{
    Q_OBJECT

public:
    IntroWindow(QWidget *parent = nullptr);
    ~IntroWindow();

private:
    Ui::IntroWindow *ui;
};
#endif // INTROWINDOW_H
