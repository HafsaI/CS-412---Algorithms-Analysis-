# CS 412 Algorithms & Analysis

You are given n eggs and a building with k floors. Dropping an egg from a floor higher than the threshold floor will break the egg. A drop from a floor equal to or lower than the threshold floor conserves the egg. Given that an unbroken egg can be dropped from any floor, what is the minimum number of egg drops D needed in order to find the threshold floor in the worst case? \\
\\
\textbf{Constraints}:
\begin{enumerate}
\item An egg that survives a fall can be used again.
\item A broken egg must be discarded.
\item The effect of a fall is the same for all eggs.
\item If an egg breaks when dropped, then it would break if dropped from a higher floor.
\item If an egg survives a fall then it would survive a shorter fall
\end{enumerate}
We will be comparing three approaches to solve this problem.
\begin{itemize}
  \item Recursive
  \item Dynamic Programming
  \item Binomial Coefficients With Binary Search
\end{itemize}
\section{Applications} 
\begin{enumerate}
    \item  Minimizing cache misses when retrieving data from the cache \cite{brilliant}
    \item  Performing a large number of queries on a database \cite{brilliant}
    \item Avoiding a call to the HDD which is slower \cite{brilliant}
\end{enumerate}
