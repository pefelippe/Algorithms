#include <iostream>


struct noh{
	int chave;
	int valor;
};

noh inserir(int chave, int valor){
	noh p;
	p.chave = chave;
	p.valor = valor;
	return p;
}  
int main(int argc, char const *argv[])
{
	noh p[5];
	p[0] = inserir(10, 30);
	return 0;
}