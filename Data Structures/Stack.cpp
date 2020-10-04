#include <iostream>
#include <new>
using namespace std;

template <typename T>
struct Noh
{
	T elem;
	Noh<T> *prox;
};

template <typename T>
struct Pilha{
	Noh <T> *topo;
};

template <typename T>
bool empilhar(Pilha<T> &P, T e){
	Noh <T> *n = new Noh <T>;
	if (n == nullptr) return false;
	n->elem = e;
	n->prox = P.topo;
	P.topo = n;
	return true;
}

template <typename T>
T desempilhar (Pilha<T> &P){
	Noh <T> *aux = P.topo;
	delete P.topo;
	P.topo = aux->prox;
	return aux->elem;

}
template <typename T>
bool vazia(Pilha<T> &P){
	return (P.topo == nullptr);
}

template <typename T>
void printar(Pilha<T> &P){
	Noh<T> *aux = P.topo;
	cout << aux->elem << "-";
	while(aux->prox != nullptr){

		aux = aux->prox;
		cout << aux->elem << "-";

	}
}


template <typename T>
void inicializar(Pilha<T> &P){
		P.topo = nullptr;
}
int main(int argc, char const *argv[])
{
	Pilha<int> P;

	inicializar(P);
	empilhar(P, 10);
	empilhar(P, 20);
	empilhar(P, 30);
	empilhar(P, 40);
	empilhar(P, 50);
	empilhar(P, 60);
	desempilhar(P);
	
	printar(P);
	return 0;
}