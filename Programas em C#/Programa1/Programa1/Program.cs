using System;

namespace curso
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Olá mundo!");  // O comando Console.WriteLine provoca uma quebra de linha.
            Console.WriteLine("Bom dia!");   // Se fosse apenas Console.Write, os argumentos "Olá Mundo!" e "Bom dia!" apareceriam
                                             // na mesma linha
            Console.ReadLine();
        }
    }
}