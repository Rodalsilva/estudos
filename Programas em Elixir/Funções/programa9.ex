defmodule Racional_algebrico do
  def racional(p, x), do: quociente(1, p*x)
  defp quociente(a, b), do: (-1)*(a/b)
end
