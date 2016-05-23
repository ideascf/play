package main

import "github.com/astaxie/beego"

type MainController struct {
	beego.Controller
}

func (this *MainController) Get() {
	this.Ctx.WriteString("hello world")
}

func main() {
	beego.BConfig.Listen.HTTPPort = 8888
	beego.Router("/", &MainController{})
	beego.Run()
}
