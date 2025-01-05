defmodule Subtracao do
  defmodule Quadrado do
    def quadrado(x), do: subtracao(x*x, 1)
    defp subtracao(a, b), do: a - b
  end
end
defmodule Subtracao.Quadrado do
  def div(x) do
    x/(x*x - 1)
  end
end
