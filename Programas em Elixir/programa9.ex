defmodule Racional_algebrico do
  def racional(p, x), do: quociente(1, p*x)
  defp quociente(a, b), do: a/b
end
