#!/usr/bin/python3
import pywikibot

# repo = pywikibot.Site("wikidata", "wikidata").data_repository()
def follow_links_to_label(node_id, links):
    initial_node = pywikibot.ItemPage(repo, node_id)
    return follow_links_to_label_repo(initial_node, links, repo)

def follow_links_to_label_repo(node, links, repo):
    repo = pywikibot.Site("wikidata", "wikidata").data_repository()
    item_dict = node.get()
    if len(links) > 0:
        labels = []
        clm_dict = item_dict["claims"]
        if links[0] in clm_dict:
            clm_list = clm_dict[links[0]]
            for clm in clm_list:
                # This is the party
                if clm.getTarget():
                    labels.append(follow_links_to_label_repo(clm.getTarget(), links[1:], repo))
        return labels
    else:
        # Get label
        if 'labels' in item_dict and 'en' in item_dict['labels']:
            return item_dict['labels']['en']
        else:
            return None
