import pywikibot

def follow_links_to_label(node_id, links):
    """
    Wrapper function of the follow_links_to_label_repo function handling
    initialisation.
    """
    repo = pywikibot.Site("wikidata", "wikidata").data_repository()
    initial_node = pywikibot.ItemPage(repo, node_id)
    return follow_links_to_label_repo(initial_node, links, repo)

def follow_links_to_label_repo(node, links, repo):
    """
    Finds wikidata paths starting from node_id and following the properties
    listed in 'links' and returns the labels of the nodes at the end of those paths.
    :param node_id: id of the starting node in the wikidata
    :param political_alignment: list of wikidata properties that lead to the labels
    :param repo: wikidata repo where the data will be pulled from
    :return: list with the labels of the end nodes.
    """
    item_dict = node.get()
    # Recursively follow the path
    if len(links) > 0:
        labels = []
        clm_dict = item_dict["claims"]
        if links[0] in clm_dict:
            clm_list = clm_dict[links[0]]
            for clm in clm_list:
                if clm.getTarget():
                    labels.append(follow_links_to_label_repo(clm.getTarget(), links[1:], repo))
        return labels
    else:
        # Base case so find the label and return
        if 'labels' in item_dict and 'en' in item_dict['labels']:
            return item_dict['labels']['en']
        else:
            return None
