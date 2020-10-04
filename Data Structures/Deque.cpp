#include <iostream>

using namespace std;
template <typename T>
struct Noh
{
	T elem;
	Noh<T> *ant, *prox;
};

template <typename T>
struct Deque
{
	Noh<T> *dir, *esq;
};

template <typename T>
void inicializar(Deque<T> &D)
{
	D.dir = nullptr;
	D.esq = nullptr;
}

template <typename T>
bool enfilar_esq(Deque<T> &D, T e)
{
	Noh<T> *n = new Noh <T>;
	if (n == nullptr) return false;
	n->elem = e;
	n->prox = D.esq;
	n->ant = nullptr;
	if (D.esq == nullptr && D.dir == nullptr){
		D.dir = D.esq = n;
	} else {
		D.esq = n;
		n->prox->ant = n;
	}
	return true;
}

template <typename T>
T remover_esq (Deque<T> &D)
{
	Noh<T> *n = D.esq;
	T e = n->elem;

	D.esq = n->prox;
	if (D.esq == nullptr){
		D.dir == nullptr;
	}
	else{
		D.esq->ant = nullptr;
	}

	delete n;
	return e;
}

template <typename T>
T consultar_esq (Deque <T> &D)
{
	return D.esq->elem;
}

template <typename T>
void printar(Deque<T> &D)
{
	Noh<T> *n = D.esq;
	while(n != nullptr){
		cout << n->elem << " ";
		n = n->prox;
	}
}

int main(int argc, char const *argv[])
{
	Deque<int> D;
	inicializar(D);
	enfilar_esq(D, 10);
	enfilar_esq(D, 20);
	remover_esq(D);
	enfilar_esq(D,30);
	printar(D);
	return 0;
}