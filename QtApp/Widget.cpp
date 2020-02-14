#include "Widget.h"
#include "ui_Widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}




void Widget::on_spinBoxWork_valueChanged(const QString &arg1)
{

}

void Widget::on_spinBoxRest_valueChanged(const QString &arg1)
{

}
