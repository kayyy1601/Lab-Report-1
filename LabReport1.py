#BFS
graph = {
    'A': ['D', 'B'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'G': ['F'],
    'H': ['G', 'F'],
    'F': []
}

def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)

            for neighbor in sorted(graph[node]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited
print("BFS alphabetical:", bfs('A'))

#DFS
graph = {
    'A': ['D', 'B'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'G': ['F'],
    'H': ['G', 'F'],
    'F': []
}

def dfs(start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

print("DFS alphabetical:", dfs('A'))



# ----- STREAMlit UI -----
import streamlit as st
st.title("Graph Traversal: BFS & DFS")
st.write("This app performs BFS and DFS on a predefined graph.")

st.subheader("Graph Structure")
st.json(graph)

start_node = st.selectbox("Choose Starting Node:", list(graph.keys()))

if st.button("Run Traversals"):
    bfs_result = bfs(start_node)
    dfs_result = dfs(start_node)

    st.subheader("BFS (Alphabetical)")
    st.write(bfs_result)

    st.subheader("DFS (Alphabetical)")
    st.write(dfs_result)