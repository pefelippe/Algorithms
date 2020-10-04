#include <iostream>

using namespace std;

template <typename TC, typename TV>
struct Par{
	TC x;
	TV y;
};

template <typename TC, typename TV>
struct noh{
	TC chave;
	TV valor;
	noh<TC, TV> *prox;
};

template <typename TC, typename TV>
struct Dicionario{
	noh<TC, TV> *inicio;
};

template <typename TC, typename TV>
void inic(Dicionario<TC, TV> &D){
	D.inicio = nullptr;
}

template <typename TC, typename TV>
bool inserir(Dicionario<TC, TV> &D, TC chave, TV valor)
{
	noh<TC, TV> *n = new noh<TC, TV>;
	if (n == nullptr) return false;
	n->chave = chave;
	n->valor = valor;
	if(D.inicio == nullptr){
		D.inicio = n;

	} else{
		n->prox = D.inicio;
		D.inicio = n;
	}
}
template <typename TC, typename TV>
Par<bool, TV> buscar (Dicionario<TC, TV> &D, TC chave)
{
	Par<bool,TV> par;
	noh<TC, TV> *n = D.inicio;

	while(n != nullptr){
		if (n->chave == chave){
			par.x = true;
			par.y = n->valor;
			return par;
		}
		n = n->prox;
	}
	par.x = false;
	return par;
}


template <typename TC, typename TV>
bool remover (Dicionario<TC, TV> &D, TC chave)
{
	noh<TC,TV> *n = D.inicio;

	while(n->prox != nullptr){
		if(n->prox->chave == chave){
			noh<TC, TV> *aux = n->prox;
			n->prox = n->prox->prox;
			delete aux;
			return true;
		}
		n = n->prox;
	}
	return false;
}

template <typename TC, typename TV>
void printar(Dicionario<TC, TV> &D){
	noh<TC, TV> *n = D.inicio;

	while(n != nullptr){
		cout << n->valor << " ";
		n = n->prox;
	}
}

int main(int argc, char const *argv[])
{
	Dicionario <int, int> D;
	inic(D);
	inserir(D, 1, 10);
	inserir(D, 2, 20);
	inserir(D, 3, 30);
	inserir(D, 4, 40);
	remover(D, 1);

	printar(D);
	return 0;
}