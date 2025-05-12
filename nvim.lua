--require 'paths'

--print("hello from local nvim.lua")
--vim.keymap.set({'n', 'v', 'i'}, "<C-b>","<cmd>w<CR><cmd>! ./brun.sh<CR>")
vim.keymap.set({ "n", "v", "i" }, "<C-s>", function()
	vim.cmd(":stopinsert")
	vim.cmd(":w")
end)

vim.keymap.set({ "n", "v", "i" }, "<C-q>", "<cmd>q<CR>")

--vim.keymap.set({ "n", "v", "i" }, "<F5>", "<cmd>term ./brun.sh<cr>")

vim.keymap.set({ "n", "v" }, "<leader>c", ":! lgit 'now'<CR>")

--vim.cmd(":Neotree reveal_file=src/main.cpp")

vim.keymap.set({ "n", "v" }, "[", "<cmd>next tab<CR>")
vim.keymap.set({ "n", "v" }, "]", "<cmd>previous tab<CR>")

vim.keymap.set({ "n", "v", "i" }, "<C-b>", function()
	vim.cmd("stopinsert")
	vim.cmd(":w")
	vim.cmd("!./brun.sh")
end)

vim.keymap.set({ "n", "v", "i" }, "<C-d>", function()
	vim.cmd("stopinsert")
	vim.cmd(":w")
	--vim.cmd("!brun2.sh" .. " " .. vim.fn.expand("%"))
	local command = "!brun2.sh " .. vim.fn.expand("%")
	--print(command)
	--vim.cmd(command)
end)
vim.cmd(":colorscheme catppuccin")
--vim.cmd(":colorscheme blue")
--print("all done")
--vim.cmd(":e src/main.cpp")
