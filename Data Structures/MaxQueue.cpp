#include <iostream>
#include <new>

template <typename T> 
struct noh{
	T elem;
	noh <T> *prox;
};

template <typename T> 
struct FilaMaximo{
	noh<T> *inicio;
	noh<T> *fim;
	noh<T> *max;
};

template <typename T> void inicializar (FilaMaximo<T> &F){
	F.inicio = nullptr;
	F.fim = nullptr;
	F.max = nullptr;
}

template <typename T> 
bool enfilar (FilaMaximo<T> &F, T e)
{
	noh<T> *novo = new noh<T>;
	if (novo == nullptr) return -1;
	novo->valor = e;
	novo->prox = F.inicio;
	if (F.inicio == nullptr){
		F.fim = novo;
		F.max = novo->elem;
	}
	else{
		if (e > F.max){
			F.max = novo->elem;
		}
	
	}
	F.inicio = novo;
}

int main(int argc, char const *argv[])
{
	return 0;
}