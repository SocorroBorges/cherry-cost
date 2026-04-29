document.addEventListener("DOMContentLoaded", function () {

    document.querySelectorAll(".btn-editar").forEach(botao => {
        botao.addEventListener("click", function (event) {
            event.preventDefault()

                const id = this.dataset.id
                const nome = this.dataset.nome
                const custo = this.dataset.custo
                const unidade = this.dataset.unidade

                abrirModal(id, nome, custo, unidade)
        })
    })
})

function abrirModal(id, nome, custo, unidade) {
    const modal = document.getElementById("modal")
    modal.classList.add("ativo")

    document.getElementById("edit-id").value = id
    document.getElementById("edit-nome").value = nome
    document.getElementById("edit-custo").value = custo
    document.getElementById("edit-unidade").value = unidade
}

function fecharModal() {
    document.getElementById("modal").classList.remove("ativo")
}

function salvarEdicao() {
    const id = document.getElementById("edit-id").value
    const nome = document.getElementById("edit-nome").value
    const custo = document.getElementById("edit-custo").value
    const unidade = document.getElementById("edit-unidade").value

    fetch("/editar_inline", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: id,
            nome: nome,
            custo_unitario: custo,
            unidade_medida: unidade
        })
    })
    .then(() => {
        fecharModal()    

        // atualizar a tabela manualmente
        const linha = document.querySelector(`tr[data-id="${id}"]`)

        linha.children[0].innerText = nome
        linha.children[1].innerText = custo
        linha.children[2].innerText = unidade
    })
}
