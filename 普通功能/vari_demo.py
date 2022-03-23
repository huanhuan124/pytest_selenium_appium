
class Vari_demo:
    gof = "123"
    def testa(self):
        t_gof = self.gof
        print("方法内的变量："+t_gof)
        print("类变量" +self.gof)


va = Vari_demo()
va.testa()