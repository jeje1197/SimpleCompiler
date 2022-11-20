	.file	"desktop.cc"
gcc2_compiled.:
___gnu_compiled_cplusplus:
.text
	.align 4
.globl _addStrings__FPcN20
	.def	_addStrings__FPcN20;	.scl	2;	.type	32;	.endef
_addStrings__FPcN20:
	pushl %ebp
	movl %esp,%ebp
	movl 8(%ebp),%eax
	pushl %eax
	movl 16(%ebp),%eax
	pushl %eax
	call _strcat
	addl $8,%esp
	movl 12(%ebp),%eax
	pushl %eax
	movl 16(%ebp),%eax
	pushl %eax
	call _strcat
	addl $8,%esp
	movl 16(%ebp),%edx
	movl %edx,%eax
	jmp L1
	.p2align 4,,7
L1:
	movl %ebp,%esp
	popl %ebp
	ret
	.def	___main;	.scl	2;	.type	32;	.endef
LC0:
	.ascii "\0"
	.def	_memset;	.scl	2;	.type	32;	.endef
LC1:
	.ascii "pcsell\0"
LC2:
	.ascii "%s\12\0"
	.align 4
.globl _main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl %ebp
	movl %esp,%ebp
	subl $80,%esp
	call ___main
	movb LC0,%al
	movb %al,-80(%ebp)
	leal -79(%ebp),%eax
	pushl $79
	pushl $0
	pushl %eax
	call _memset
	addl $12,%esp
	pushl $LC1
	pushl $LC2
	call _printf
	addl $8,%esp
	xorl %eax,%eax
	jmp L2
	xorl %eax,%eax
	jmp L2
	.p2align 4,,7
L2:
	movl %ebp,%esp
	popl %ebp
	ret
	.def	_printf;	.scl	3;	.type	32;	.endef
	.def	_strcat;	.scl	3;	.type	32;	.endef
