{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Punto3_factorial.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPtC7ZvtmBZtvC3amE9Ynlb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/salopezn/Metodos1_MariaAlaimo_SalomeLopez/blob/Salo/Punto3_factorial.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PF63aaRdWqL-",
        "outputId": "164d9437-598b-4540-92f0-39f285902b90"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ],
      "source": [
        "def factorial(b):\n",
        "  fact=0\n",
        "  if b==0 or b==1:\n",
        "    fact=1\n",
        "  if b<0:\n",
        "    print(\"Error\")\n",
        "  else:\n",
        "    fact =1\n",
        "    for i in range(1,b+1):\n",
        "      fact=fact*i\n",
        "  return fact\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def fact_varios(x):\n",
        "  lista=[]\n",
        "  for i in range(x+1):\n",
        "    fact=factorial(i)\n",
        "    lista.append(fact)\n",
        "  print(lista)\n",
        "\n",
        "fact_varios(20)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fg3RasWNkODX",
        "outputId": "e40c90e5-0812-4950-bf5c-523cad8856da"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]\n"
          ]
        }
      ]
    }
  ]
}