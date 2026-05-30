typedef struct ListNode {
    int val;
    struct ListNode *next;
} t_node;


t_node	*list_fuse(t_node *list1, t_node *list2)
{
	t_node	*current = list1;

	while (current->next)
		current = current->next;

	current->next = list2;

	return(list1);
}


t_node* mergeTwoLists(t_node* list1, t_node* list2)
{
	t_node	*new_list;

	new_list = list_fuse(list1, list2);
	t_node	*i = new_list;
	t_node	*j = new_list->next;
	t_node	*temp;
	while(i->next)
	{
		while(j && j->next)
		{
			if (i->val > j->val)
			{
				temp->val = j->val;
				j->val = i->val;
				i->val = temp->val;
			}
			j = j->next;
		}
		i = i->next;
	}

	return (new_list);
}
